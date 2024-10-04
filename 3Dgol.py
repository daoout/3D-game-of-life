import numpy as np
from numba import njit, prange
import plotly.graph_objects as go
import plotly.io as pio
import webbrowser
import os
import random

# 设置Plotly渲染器
pio.renderers.default = 'browser'

# 初始配置生成函数
def generate_random_active_cells(size, density=0.05):
    """
    生成随机活细胞配置。
    """
    active_cells = []
    total_cells = size[0] * size[1] * size[2]
    num_active = int(total_cells * density)
    
    for _ in range(num_active):
        x = random.randint(0, size[0] - 1)
        y = random.randint(0, size[1] - 1)
        z = random.randint(0, size[2] - 1)
        active_cells.append((x, y, z))
    
    return active_cells

def generate_spherical_active_cells(size, radius=10):
    """
    生成球形活细胞配置。
    """
    active_cells = []
    center = (size[0] // 2, size[1] // 2, size[2] // 2)
    
    for x in range(size[0]):
        for y in range(size[1]):
            for z in range(size[2]):
                distance = np.sqrt((x - center[0])**2 + (y - center[1])**2 + (z - center[2])**2)
                if distance <= radius:
                    active_cells.append((x, y, z))
    
    return active_cells

def generate_spiral_active_cells(size, turns=5, spacing=5):
    """
    生成螺旋形活细胞配置。
    """
    active_cells = []
    center_x, center_y, center_z = size[0] // 2, size[1] // 2, size[2] // 2
    max_radius = min(center_x, center_y, center_z) - 1
    points_per_turn = 100  # 增加螺旋的细腻程度
    
    for turn in range(turns * points_per_turn):
        angle = (2 * np.pi * turn) / points_per_turn
        radius = (max_radius / (turns * points_per_turn)) * turn
        x = int(center_x + radius * np.cos(angle))
        y = int(center_y + radius * np.sin(angle))
        z = (center_z + (turn // points_per_turn) * spacing) % size[2]
        if 0 <= x < size[0] and 0 <= y < size[1] and 0 <= z < size[2]:
            active_cells.append((x, y, z))
    
    return active_cells

def generate_honeycomb_active_cells(size, layer_spacing=3, hex_size=5):
    """
    生成蜂窝结构活细胞配置。
    """
    active_cells = []
    center_x, center_y, center_z = size[0] // 2, size[1] // 2, size[2] // 2
    
    for layer in range(-hex_size, hex_size + 1):
        z = center_z + layer * layer_spacing
        if 0 <= z < size[2]:
            for i in range(-hex_size, hex_size + 1):
                for j in range(-hex_size, hex_size + 1):
                    if abs(i) + abs(j) <= hex_size:
                        x = center_x + i
                        y = center_y + j
                        if 0 <= x < size[0] and 0 <= y < size[1]:
                            active_cells.append((x, y, z))
    
    return active_cells

def generate_multiple_cubes_active_cells(size, cube_size=5, positions=None):
    """
    生成多个立方体活细胞配置。
    """
    if positions is None:
        positions = [
            (size[0]//4, size[1]//4, size[2]//4),
            (3*size[0]//4, 3*size[1]//4, 3*size[2]//4),
            (size[0]//4, 3*size[1]//4, size[2]//4),
            (3*size[0]//4, size[1]//4, 3*size[2]//4),
        ]
    
    active_cells = []
    
    for pos in positions:
        x_center, y_center, z_center = pos
        for x in range(x_center - cube_size//2, x_center + cube_size//2 + 1):
            for y in range(y_center - cube_size//2, y_center + cube_size//2 + 1):
                for z in range(z_center - cube_size//2, z_center + cube_size//2 + 1):
                    if 0 <= x < size[0] and 0 <= y < size[1] and 0 <= z < size[2]:
                        active_cells.append((x, y, z))
    
    return active_cells

# 模拟函数
@njit(parallel=True)
def count_neighbors(grid):
    neighbors = np.zeros(grid.shape, dtype=np.int8)
    directions = [
        (dx, dy, dz)
        for dx in (-1, 0, 1)
        for dy in (-1, 0, 1)
        for dz in (-1, 0, 1)
        if not (dx == 0 and dy == 0 and dz == 0)
    ]
    
    for dx, dy, dz in directions:
        shifted = np.zeros_like(grid)
        if dx > 0:
            shifted[dx:, :, :] = grid[:-dx, :, :]
        elif dx < 0:
            shifted[:dx, :, :] = grid[-dx:, :, :]
        else:
            shifted[:, :, :] = grid[:, :, :]
        
        if dy > 0:
            shifted[:, dy:, :] = shifted[:, :-dy, :]
        elif dy < 0:
            shifted[:, :dy, :] = shifted[:, -dy:, :]
        
        if dz > 0:
            shifted[:, :, dz:] = shifted[:, :, :-dz]
        elif dz < 0:
            shifted[:, :, :dz] = shifted[:, :, -dz:]
        
        neighbors += shifted
    
    return neighbors

@njit(parallel=True)
def evolve(grid):
    neighbors = count_neighbors(grid)
    new_grid = np.zeros(grid.shape, dtype=np.int8)
    
    for x in prange(grid.shape[0]):
        for y in prange(grid.shape[1]):
            for z in prange(grid.shape[2]):
                if grid[x, y, z] == 1:
                    # 存活规则：5到7个活邻居
                    if 5 <= neighbors[x, y, z] <= 7:
                        new_grid[x, y, z] = 1
                else:
                    # 诞生规则：5到7个活邻居
                    if 5 <= neighbors[x, y, z] <= 7:
                        new_grid[x, y, z] = 1
    return new_grid

def initialize_grid(size, active_cells):
    """
    初始化三维网格。
    """
    grid = np.zeros(size, dtype=np.int8)
    for cell in active_cells:
        x, y, z = cell
        if 0 <= x < size[0] and 0 <= y < size[1] and 0 <= z < size[2]:
            grid[x, y, z] = 1
    return grid

def run_simulation(size, active_cells, generations):
    """
    运行三维生命游戏模拟。
    """
    grid = initialize_grid(size, active_cells)
    history = [grid.copy()]
    for gen in range(generations):
        grid = evolve(grid)
        history.append(grid.copy())
        live_cells = np.sum(grid)
        print(f"Generation {gen + 1} completed. Live cells: {live_cells}")
        if live_cells == 0:
            print("所有细胞已死亡，模拟提前结束。")
            break
    return history

# 可视化函数
def create_3d_scatter(x, y, z, color='blue', size=2, opacity=0.8):
    """
    创建Plotly的3D散点图对象。
    """
    return go.Scatter3d(
        x=x,
        y=y,
        z=z,
        mode='markers',
        marker=dict(
            size=size,
            color=color,
            opacity=opacity
        )
    )

def visualize_simulation(history, save_html=True, filename="3D_Game_of_Life.html"):
    """
    可视化三维生命游戏的模拟结果，并添加滑块控制代数。
    """
    frames = []
    colors = []
    max_generations = len(history)
    
    # 生成每一代的帧
    for i, grid in enumerate(history):
        x, y, z = np.where(grid == 1)
        color = np.full(x.shape, i % 20)  # 不同代数使用不同颜色
        scatter = create_3d_scatter(x, y, z, color=color, size=3, opacity=0.8)
        frame = go.Frame(data=[scatter], name=str(i))
        frames.append(frame)
        colors.append(color)
    
    # 创建滑块步
    sliders = [dict(
        active=0,
        currentvalue={"prefix": "Generation: "},
        pad={"b": 10},
        steps=[dict(
            args=[[str(i)], dict(frame=dict(duration=300, redraw=True), mode="immediate", transition=dict(duration=0))],
            label=str(i),
            method="animate"
        ) for i in range(len(frames))]
    )]
    
    # 创建布局
    fig = go.Figure(
        data=[frames[0].data[0]],
        layout=go.Layout(
            sliders=sliders,
            updatemenus=[dict(
                type="buttons",
                buttons=[
                    dict(label="Play",
                         method="animate",
                         args=[None, {"frame": {"duration": 300, "redraw": True},
                                      "fromcurrent": True, "transition": {"duration": 0}}]),
                    dict(label="Pause",
                         method="animate",
                         args=[[None], {"frame": {"duration": 0, "redraw": False},
                                        "mode": "immediate",
                                        "transition": {"duration": 0}}])
                ],
                pad={"r": 10, "t": 10},
                showactive=False,
                x=0.1,
                xanchor="right",
                y=0,
                yanchor="top"
            )],
            scene=dict(
                xaxis=dict(range=[0, history[0].shape[0]], autorange=False, title='X'),
                yaxis=dict(range=[0, history[0].shape[1]], autorange=False, title='Y'),
                zaxis=dict(range=[0, history[0].shape[2]], autorange=False, title='Z'),
                aspectmode='cube'
            ),
            title="3D生命游戏模拟"
        ),
        frames=frames
    )
    
    if save_html:
        fig.write_html(filename)
        print(f"Visualization saved to {filename}")
        filepath = os.path.abspath(filename)
        webbrowser.open('file://' + filepath)
        # 保持脚本运行，直到用户手动关闭浏览器或按下Enter键
        input("模拟完成。按 Enter 键退出程序并关闭脚本。")
    else:
        fig.show()

# 主函数
def main():
    size = (100, 100, 100)  # 长宽高各扩大1倍，空间总大小扩大8倍
    random_active_cells = generate_random_active_cells(size, density=0.03)
    multiple_cubes_active_cells = generate_multiple_cubes_active_cells(size, cube_size=5)
    spherical_active_cells = generate_spherical_active_cells(size, radius=10)
    spiral_active_cells = generate_spiral_active_cells(size, turns=5, spacing=5)
    honeycomb_active_cells = generate_honeycomb_active_cells(size, layer_spacing=3, hex_size=5)
    
    # 合并不同的初始配置
    active_cells = (
        random_active_cells +
        multiple_cubes_active_cells +
        spherical_active_cells +
        spiral_active_cells +
        honeycomb_active_cells
    )
    
    print(f"初始化活细胞数量: {len(active_cells)}")
    
    generations = 30  # 增加代数以观察更丰富的变化
    history = run_simulation(size, active_cells, generations)
    
    visualize_simulation(history, save_html=True, filename="3D_Game_of_Life_Expanded_Rich.html")

if __name__ == "__main__":
    main()

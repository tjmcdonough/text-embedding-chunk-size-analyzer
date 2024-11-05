import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

def create_heatmap(df: pd.DataFrame, x_col: str, y_col: str, z_col: str) -> go.Figure:
    """Create a heatmap visualization"""
    pivot_table = df.pivot(index=y_col, columns=x_col, values=z_col)
    
    fig = go.Figure(data=go.Heatmap(
        z=pivot_table.values,
        x=pivot_table.columns,
        y=pivot_table.index,
        colorscale='Viridis',
        colorbar=dict(title=z_col.replace('_', ' ').title())
    ))
    
    fig.update_layout(
        xaxis_title=x_col.replace('_', ' ').title(),
        yaxis_title=y_col.replace('_', ' ').title(),
        height=400
    )
    
    return fig

def create_line_plot(df: pd.DataFrame, x_col: str, y_col: str) -> go.Figure:
    """Create a line plot visualization"""
    fig = px.line(
        df.groupby(x_col)[y_col].mean().reset_index(),
        x=x_col,
        y=y_col,
        markers=True
    )
    
    fig.update_layout(
        xaxis_title=x_col.replace('_', ' ').title(),
        yaxis_title=y_col.replace('_', ' ').title(),
        height=400
    )
    
    return fig

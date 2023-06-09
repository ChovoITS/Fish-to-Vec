import plotly.express as px
import pandas as pd

def plot(df:pd.DataFrame, dimension:int = 3, color:str = "Order", n_neighbors:int = 5) -> None:
    '''The function plots a scatter plot of a pandas DataFrame with either 2 or 3 dimensions, with the
    option to color the points based on a specified column.
    
    Parameters
    ----------
    df : pd.DataFrame
        a pandas DataFrame containing the data to be plotted
    dimension : int, optional
        The dimension of the plot, which can be either 2 or 3.
    color : str, optional
        The parameter "color" is used to specify which column of the DataFrame should be used to color the
    points in the plot.
    
    '''

    hover_data_dict={'X':  False, 
                'Y': False, 
                'Z': False,
                "Continent": True,
                "Classification": True,
                "Order": True,
                "Family": True,
                "Temperament":  True,
                "Level": True,
                "Diet": True,
                "PH": True,    
                "GH": True,
                "Temp": True,
                "Size": True
                }
    for i in range(n_neighbors):
        hover_data_dict[f"Nearest Neighbors {i+1}"] = True
    
    if dimension == 3:
        fig = px.scatter_3d(df, x='X', y='Y', z='Z', color=color, hover_name="Common Name", 
                            category_orders={color: sorted(df[color].unique())},
                            hover_data=hover_data_dict, range_x=[-20,20], range_y=[-20, 20], range_z=[-20, 20])
        fig.update_layout(scene=dict(aspectmode='cube'))
    else:
        fig = px.scatter(df, x='X', y='Y', color=color, hover_name="Common Name", category_orders={color: sorted(df[color].unique())},
                         hover_data=hover_data_dict)

    fig.show()
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 22:12:27 2025

@author: m.lotfi
"""

def undo_explode(df, exploded_columns, group_columns=None):
    """
    Undo the effect of explode by combining values back into lists.
    
    Parameters:
    df (pandas.DataFrame): DataFrame with exploded values
    exploded_columns (str or list): Column(s) that were exploded
    group_columns (list): Columns to group by (None for all other columns)
    
    Returns:
    pandas.DataFrame: DataFrame with combined values
    """
    try:
        # Convert single column to list
        if isinstance(exploded_columns, str):
            exploded_columns = [exploded_columns]
            
        # If group_columns not specified, use all columns except exploded ones
        if group_columns is None:
            group_columns = [col for col in df.columns if col not in exploded_columns]
            
        # Group and aggregate
        agg_dict = {col: list for col in exploded_columns}
        for col in df.columns:
            if col not in exploded_columns and col not in group_columns:
                agg_dict[col] = 'first'
                
        result = df.groupby(group_columns, as_index=False).agg(agg_dict)
        
        return result
        
    except Exception as e:
        print(f"Error in undo_explode: {e}")
        return None
import plotly.graph_objects as go

labels = ['Data A', 'Data B', 'Data C', 'Data D', 'Data E', 'Data F']

source = [0, 0, 1, 1, 2, 3]
target = [2, 3, 4, 5, 4, 5]
value = [10, 5, 15, 10, 5, 10]

fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=labels,
        color="blue"
    ),
    link=dict(
        source=source,
        target=target,
        value=value
    )
)])

fig.update_layout(title_text="Sankey Diagram", font_size=10)
fig.show()
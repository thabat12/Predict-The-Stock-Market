import plotly.graph_objects as go
import pandas as pd
import numpy as np
import talib as ta
import yfinance as yf

# Download stock data from Yahoo Finance (adjust the symbol to your preference)
symbol = 'AAPL'  # Example: Apple stock
data = yf.download(symbol, start="2023-01-01", end="2024-01-01")

# Calculate RSI (Relative Strength Index)
data['RSI'] = ta.RSI(data['Close'], timeperiod=14)

# Calculate MACD (Moving Average Convergence Divergence)
data['MACD'], data['MACD_signal'], _ = ta.MACD(data['Close'], fastperiod=12, slowperiod=26, signalperiod=9)

# Create traces for the figure
trace_price = go.Scatter(x=data.index, y=data['Close'], mode='lines', name='Close Price', line=dict(color='blue'))

# RSI Trace
trace_rsi = go.Scatter(x=data.index, y=data['RSI'], mode='lines', name='RSI', line=dict(color='green'))

# Overbought and Oversold Levels for RSI
trace_rsi_overbought = go.Scatter(x=data.index, y=[70]*len(data), mode='lines', name='Overbought (70)', line=dict(color='red', dash='dash'))
trace_rsi_oversold = go.Scatter(x=data.index, y=[30]*len(data), mode='lines', name='Oversold (30)', line=dict(color='orange', dash='dash'))

# MACD Trace
trace_macd = go.Scatter(x=data.index, y=data['MACD'], mode='lines', name='MACD', line=dict(color='blue'))

# MACD Signal Line
trace_macd_signal = go.Scatter(x=data.index, y=data['MACD_signal'], mode='lines', name='Signal Line', line=dict(color='red'))

# Create subplots using make_subplots (3 rows, 1 column)
from plotly.subplots import make_subplots

fig = make_subplots(rows=3, cols=1, shared_xaxes=True, vertical_spacing=0.1, 
                    subplot_titles=[f"{symbol} Stock Price", "Relative Strength Index (RSI)", "MACD & Signal Line"],
                    row_heights=[0.5, 0.25, 0.25])

# Add stock price trace to the first subplot (row 1)
fig.add_trace(trace_price, row=1, col=1)

# Add RSI trace to the second subplot (row 2)
fig.add_trace(trace_rsi, row=2, col=1)
fig.add_trace(trace_rsi_overbought, row=2, col=1)
fig.add_trace(trace_rsi_oversold, row=2, col=1)

# Add MACD and Signal Line traces to the third subplot (row 3)
fig.add_trace(trace_macd, row=3, col=1)
fig.add_trace(trace_macd_signal, row=3, col=1)

# Update layout for aesthetics and to add axis labels
fig.update_layout(
    title=f'{symbol} Price with RSI & MACD',
    xaxis_title="Date",
    yaxis_title="Price ($)",
    yaxis2_title="RSI",
    yaxis3_title="MACD",
    xaxis_rangeslider_visible=False,
    template="plotly_dark",  # Set dark mode template for the background
    height=900,
    showlegend=True
)

# Show the plot
fig.show()

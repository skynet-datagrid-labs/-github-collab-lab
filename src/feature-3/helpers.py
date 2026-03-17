# Feature 3 helpers
# Created by jammiemwendwa-eng

def calculate_metrics(data):
    """Calculate basic metrics from input data"""
    if not data:
        return {}
    
    return {
        'count': len(data),
        'sum': sum(data),
        'average': sum(data)/len(data) if data else 0
    }

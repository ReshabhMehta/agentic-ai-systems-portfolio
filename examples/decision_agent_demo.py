

```python
def decision_agent(confidence_score):
    if confidence_score < 0.6:
        return "HOLD"
    elif confidence_score < 0.75:
        return "PROBE"
    return "PROGRESS"

scores = [0.4, 0.7, 0.85]

for s in scores:
    print(f"Score: {s} -> Action: {decision_agent(s)}")

from bitdeli.insight import insight
from bitdeli.widgets import Bar, Widget
from discodb.query import Q, Literal, Clause

class TokenInput(Widget):
    pass

@insight
def view(model, params):
    print params
    params = {'events': ['$signup', 'Clip created']}
    def steps(events):
        for i in range(len(events)):
            q = Q([Clause([Literal(event)]) for event in events[:i + 1]])
            yield events[i], len(model.query(q))
    return [TokenInput(size=(12, 1), data={'source': list(model)}),
            Bar(size=(12, 6),
                data=list(steps(params['events'])))]
    
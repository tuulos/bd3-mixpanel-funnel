from bitdeli.insight import insight, segment, segment_label
from bitdeli.widgets import Text, Bar, Table, Widget
from discodb.query import Q, Literal, Clause

class TokenInput(Widget):
    pass

class Funnel(Widget):
    pass

@segment
def segment(model, params):
    return ['1', '1000082353', '1000374994']

@segment_label
def label(segment, params):
    return '%d people' % len(segment)

@insight
def view(model, params):
    chosen = params['events']['value'] if 'events' in params else []
    def steps(events):
        for i in range(len(events)):
            q = Q([Clause([Literal(event)]) for event in events[:i + 1]])
            yield events[i], len(model.query(q))
    widgets = [TokenInput(id='events',
                          size=(12, 1),
                          label='Event Sequence',
                          value=chosen,
                          data=list(model))]
    if chosen:
        widgets += [Funnel(id='funnel',
                           size=(12, 6),
                           data=list(steps(chosen)))]
    return widgets
from django import forms

LOCATION_CHOICES = [
    ('金城鎮', '金城鎮'),
    ('金寧鄉', '金寧鄉'),
    ('烈嶼鄉', '烈嶼鄉'),
    ('金沙鎮', '金沙鎮'),
    ('金湖鎮', '金湖鎮'),
]

CASE_TYPE_CHOICES = [
    ('住宅火災', '住宅火災'),
    ('雜草火災', '雜草火災'),
    ('汽機車火災', '汽機車火災'),
]

class DispatchForm(forms.Form):
    location = forms.ChoiceField(label='案件地點', choices=LOCATION_CHOICES)
    case_type = forms.ChoiceField(label='案件類型', choices=CASE_TYPE_CHOICES)

from django import forms

from user.models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['dating_sex', 'location', 'min_distance',
                  'max_distance', 'min_dating_age',
                  'max_dating_age','vibration',
                  'only_matche', 'auto_play',
        ]

    def clean_max_dating_age(self):
        cleaned_data = super().clean()
        min_dating_age = cleaned_data.get('min_dating_age')
        max_dating_age = cleaned_data.get('max_dating_age')
        if min_dating_age > max_dating_age:
            raise forms.ValidationError('min_dating_age %s > max_dating_age %s' % (min_dating_age, max_dating_age))
        return max_dating_age

"""
为什么我们在django中的表单上使用cleaned_data
浏览 46关注 0回答 1得票数 2
原文
为什么我们使用cleaned_data firstname= form.cleaned_data.get("first_name")

这其中的意义是什么?为什么它是必要的？

原文
关注
分享
反馈
Shatish Desai
提问于2020-07-07 00:14
1 个回答
Sheraram_Prajapat
回答于2020-07-07 01:04
已采纳
得票数 2
当您在窗体上调用is_valid()方法时，它将导致验证和清除窗体数据。在此过程中，Django创建了一个名为cleaned_data的属性，这是一个字典，其中只包含已通过验证测试的字段中已清除的数据。

有两种类型:基本形式(forms.Form)和ModelForm (forms.ModelForm)。

如果您使用的是ModelForm，那么就不需要使用cleaned_data字典，因为当您执行form.save()时，它已经匹配并且保存了干净的数据。但是您使用的是基本表单，那么您必须手动将每个cleaned_data与其数据库位置进行匹配，然后将实例保存到数据库，而不是表单。

例如，基本形式：

if form.is_valid():
    ex = Example()
    ex.username = form.cleaned_data['username']
    ex.save()
复制
例如ModelForm：

if form.is_valid():
    form.save()
复制
重要提示:如果表单从is_valid()阶段通过，则没有任何未经验证的数据。
"""



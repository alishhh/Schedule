from django import forms
from sch.models import Schedule


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ('group', 'nameM1', 'typeM1', 'teacherM1', 'roomM1',
                  'nameM2', 'typeM2', 'teacherM2', 'roomM2',
                  'nameM3', 'typeM3', 'teacherM3', 'roomM3',
                  'nameM4', 'typeM4', 'teacherM4', 'roomM4',
                  'nameM5', 'typeM5', 'teacherM5', 'roomM5',
                  'nameM6', 'typeM6', 'teacherM6', 'roomM6',

                  'nameT1', 'typeT1', 'teacherT1', 'roomT1',
                  'nameT2', 'typeT2', 'teacherT2', 'roomT2',
                  'nameT3', 'typeT3', 'teacherT3', 'roomT3',
                  'nameT4', 'typeT4', 'teacherT4', 'roomT4',
                  'nameT5', 'typeT5', 'teacherT5', 'roomT5',
                  'nameT6', 'typeT6', 'teacherT6', 'roomT6',

                  'nameW1', 'typeW1', 'teacherW1', 'roomW1',
                  'nameW2', 'typeW2', 'teacherW2', 'roomW2',
                  'nameW3', 'typeW3', 'teacherW3', 'roomW3',
                  'nameW4', 'typeW4', 'teacherW4', 'roomW4',
                  'nameW5', 'typeW5', 'teacherW5', 'roomW5',
                  'nameW6', 'typeW6', 'teacherW6', 'roomW6',

                  'nameTH1', 'typeTH1', 'teacherTH1', 'roomTH1',
                  'nameTH2', 'typeTH2', 'teacherTH2', 'roomTH2',
                  'nameTH3', 'typeTH3', 'teacherTH3', 'roomTH3',
                  'nameTH4', 'typeTH4', 'teacherTH4', 'roomTH4',
                  'nameTH5', 'typeTH5', 'teacherTH5', 'roomTH5',
                  'nameTH6', 'typeTH6', 'teacherTH6', 'roomTH6',

                  'nameF1', 'typeF1', 'teacherF1', 'roomF1',
                  'nameF2', 'typeF2', 'teacherF2', 'roomF2',
                  'nameF3', 'typeF3', 'teacherF3', 'roomF3',
                  'nameF4', 'typeF4', 'teacherF4', 'roomF4',
                  'nameF5', 'typeF5', 'teacherF5', 'roomF5',
                  'nameF6', 'typeF6', 'teacherF6', 'roomF6',
                  )


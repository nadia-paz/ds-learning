import enum

class MyEnum(enum.Enum):
    here = 7
    there = 8
    everywhere = 9

# access name and value
print(f'Here name is: {MyEnum.here.name}')
print(f'There value is {MyEnum.there.value}')

# iterating through the enum object
for me in MyEnum:
    print(f'{me.name:15}= {me.value}')

# enum can not be sorted / ordered by value, use IntEnum insted

class myIntEnum(enum.IntEnum):
    there = 8
    everywhere = 9
    here = 7

print('Unsorted')
print('\n'.join(' ' + s.name for s in myIntEnum))
print()

print('Sorted')
print('\n'.join(' ' + s.name for s in sorted(myIntEnum)))
print()

# unique decorator to Enum. Accepts only unique values

@enum.unique
class MyUniqueEnum(enum.Enum):
    here = 7
    there = 8
    everywhere = 9
    # (will throw a ValueError error: duplicate values found)
    # nowhere = 9 

# programmatically create enums
MyAutoEnum = enum.Enum(
    value='AutoIncrement', # better make value = name of the class. Here is different only for educ.purposes
    names = ('first second third forth '
            'fifth')
)

for mae in MyAutoEnum:
    print(f'{mae.name:15}= {mae.value}')

print(f'2nd: {MyAutoEnum.second}') # 2nd: AutoIncrement.second
print(f'2nd value: {MyAutoEnum.second.value}') # 2nd value: 2

# mapping values
MyMappingEnum = enum.Enum(
    value ='MyMappingEnum',
    names = [
        ('first', 1),
        ('second', 2),
        ('third', 3)
    ]
)

# enums can contain non-integer values -> tuples, dictionaries
# complex values passed directly to __init__

class BugStatus(enum.Enum):
    new = (7, ['incomplete', 'invalid', 'in_progress', 'wont_fix'])
    incomplete = (6, ['new','wont_fix'])
    invalid = (5, ['new'])
    in_progress = (3, ['new'])
    wont_fix = (4, ['invalid', 'new'])

    def __init__(self, num, transitions):
        self.num = num
        self.transitions = transitions
    
    def can_transition(self, new_state):
        # if the name of the new bug in in the current bug's transitions list
        return new_state.name in self.transitions

print('BugStatus - tuples')
print('Name: ', BugStatus.in_progress)
print('Value: ', BugStatus.in_progress.value)
print('Transitions list: ', BugStatus.in_progress.transitions)
print('Can transition to the BugStatus.new: ', BugStatus.in_progress.can_transition(BugStatus.new))

# same as above but pass a dictionary to enum
class BugStatusDict(enum.Enum):
    new = {
        'num':7, 
        'transitions':['incomplete', 'invalid', 'in_progress', 'wont_fix']
    }
    incomplete = {
        'num':6, 
        'transitions':['new','wont_fix']
    }
    invalid = {
        'num':5, 
        'transitions':['new']
    }
    in_progress = {
        'num':3, 
        'transitions':['new']
    }
    wont_fix = {
        'num':4, 
        'transitions':['invalid', 'new']
    }

    def __init__(self, vals):
        self.num = vals['num']
        self.transitions = vals['transitions']
    
    def can_transition(self, new_state):
        # if the name of the new bug in in the current bug's transitions list
        return new_state.name in self.transitions

print('BugStatus - dictionaries')
print('Name: ', BugStatusDict.in_progress)
print('Value: ', BugStatusDict.in_progress.value)
print('Transitions list: ', BugStatusDict.in_progress.transitions)
print('Can transition to the BugStatus.new: ', BugStatusDict.in_progress.can_transition(BugStatus.new))
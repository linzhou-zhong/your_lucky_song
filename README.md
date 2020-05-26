
# Find the Number 1 Song on the Day You Were Born
A python class and main function to find the most played song on the day you were born.

## Installation
### Requirements

You should preferer Python 3 packages from your operating system.

### Install the module
Under Windows and MacOs:


```shell
pip3 install your_day_song
```
If you meet per;issions issue, I recommend you try this step:

```shell
pip3 install your_day_song --user
```

### Into a Python program
```python
from your_day_song import your_day_song as yds

user = yds(dday=None, month=None, year=None)
url = user.feel_lucky()
```

Where `yds` is used to get the date you were born, and to get your lucky song from `feel_lucky` right now !. 


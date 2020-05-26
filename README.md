
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
If you meet permissions issue, I recommend you try this step:

```shell
pip3 install your_day_song --user
```

### Into a Python program
Remember to replace `day`, `month` and `year` in bracket with your favorite number. \
Ex : `user = yls(day=1, month=1, year=1990)`
```python
from your_lucky_song import your_lucky_song as yls

user = yls(day=None, month=None, year=None)
url = user.feel_lucky()
```

Where `yds` is used to get the date you were born, `feel_lucky()` will give you directly a url from Youtube and to export your lucky right now !. 


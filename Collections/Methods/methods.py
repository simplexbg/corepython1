#1. append() - Add an element at the end of the list
social_media = ['facebook','instagram','twitter']
social_media.append('linkedin')
print(social_media)
#['facebook', 'instagram', 'twitter', 'linkedin']

#2. clear() -Remove all the elements from the list
social_media = ['facebook','instagram','twitter']
social_media.clear()
print(social_media)
#[]
#3 3. copy() -Make a copy of the list

social_media = ['facebook','instagram','twitter']
new_list=social_media.copy()
print(new_list)
#['facebook', 'instagram', 'twitter']

#4 count()-Count the frequency of a particular element with
#the specified value.
sm=['facebook','linkedin','instagram','twitter','linkedin']
res=sm.count("linkedin")
print(res)
#2

#5 -extend()-Add the elements of a list (or any iterable), to the
#end of the current list

social_media=['facebook','twitter']
education=['udemy','coursera']
social_media.extend(education)
print(social_media)
#['facebook', 'twitter', 'udemy', 'coursera']
#6. insert() -Add an element at the specified position.
social_media = ['facebook','instagram','twitter']
social_media.insert(0,"linkedin")
print(social_media)
#['linkedin', 'facebook', 'instagram', 'twitter']
#7. pop(), Remove the element from the specified position
social_media = ['facebook','instagram','twitter']
social_media.pop(1)
print(social_media)
#['facebook', 'twitter']

#8. remove()-Remove the first item with the specified value
social_media = ['facebook','instagram','twitter']
social_media.remove('facebook')
print(social_media)
#['instagram', 'twitter']
#9 reverse()-Reverse the order of the list
social_media = ['facebook','instagram','twitter']
social_media.reverse()
print(social_media)
#['twitter', 'instagram', 'facebook']
#10. sort()-Sort the list in increasing and decreasing order.
number=[10,44,21,8]
number.sort()
number.sort(reverse=True)
print(number)
#[44, 21, 10, 8]



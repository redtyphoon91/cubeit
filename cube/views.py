from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Cube, Content, User,CubeContent,UserCont
import json

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

# creating a user
def user(request,name,city):
    if(User.objects.filter(name=name)):
        return HttpResponse("This user already exists")

    u = User(name=name,city=city)
    u.save()
    user = {}
    user["id"] = u.id
    user["name"] = name
    user["city"] = city

    return HttpResponse(json.dumps(user))

# creating a cube, #9 get all cube for a user
def cube(request, userid,name):
    #checking if user with userid exists
    
    try:
    	user = User.objects.get(id=userid)
    except User.DoesNotExist:
        return HttpResponse("This user does not exist, proceed with user creation first ")

    c = Cube(name=name)
    c.save()

    #creating entry in user for associated cube
    user.cubeid = c.id
    user.save()

    cube = {}
    cube["id"] = c.id
    cube["user-id"] = userid
    cube["name"] = name


    return HttpResponse(json.dumps(cube))
    
#3 For creating a content for a user, #10 For listing all contents of a user
def content(request,userid,link):
    #checking if user with userid exists
    try:
        user = User.objects.get(id=userid)
    except User.DoesNotExist:
        return HttpResponse("This user does not exist, proceed with user creation first ")


    c = Content(link=link)
    c.save()

    #creating entry in user for associated content
    userC = UserCont(Contentid = c.id,Useri=userid)
    userC.save()

    content = {}
    content["id"] = c.id
    content["user-id"] = userid
    content["link"] = link


    return HttpResponse(json.dumps(content))

# For adding a content to a cube
def contentcube(request,userid,cubeid,contentid):
	#add try catch blocks 
	try:
		user = User.objects.get(id=userid)
	except User.DoesNotExist:
		return HttpResponse("This user does not exist, proceed with user creation first ")
	
	try:
		cube = Cube.objects.get(id=cubeid)
	except Cube.DoesNotExist:
		return HttpResponse("This cube does not exist, proceed with cube creation first ")	
	
	if(user.cubeid != cube.id):
		return HttpResponse("This cube does not exist for this user")
		

	c = CubeContent(Cubeid  = cube.id,Contentid =contentid)
	c.save()
	cc = {}
	cc["cube-id"] = cube.id
	cc["content-id"] = contentid

	return HttpResponse(json.dumps(cc))

# deleting a content from a cube
def delete_cube(request,userid,cubeid):
	#add try catch blocks 
	try:
		user = User.objects.get(id=userid)
	except User.DoesNotExist:
		return HttpResponse("This user does not exist, proceed with user creation first ")
	
	try:
		cube = Cube.objects.get(id=cubeid)
	except Cube.DoesNotExist:
		return HttpResponse("This cube does not exist, proceed with cube creation first ")
	
	CubeContent.objects.filter(id = cubeid).delete()
	for user in User.objects.filter(cubeid = cubeid):
		user.cubeid = ""
	
	return HttpResponse("deleted cube")

# deleting a content from a cube
def contentcubedelete(request,userid,cubeid,contentid):
	#add try catch blocks 
	try:
		user = User.objects.get(id=userid)
	except User.DoesNotExist:
		return HttpResponse("This user does not exist, proceed with user creation first ")
	
	try:
		cube = Cube.objects.get(id=cubeid)
	except Cube.DoesNotExist:
		return HttpResponse("This cube does not exist, proceed with cube creation first ")

	try:
		content = Content.objects.get(id=contentid)
	except Content.DoesNotExist:
		return HttpResponse("This content does not exist, proceed with content creation first ")	
	
	CubeContent.objects.filter(Contentid = contentid).delete()
	
	return HttpResponse("deleted content")


# sharing a cube with other user
def share_cube(request,userid,cubeid,newuserid):
	try:
		user = User.objects.get(id=userid)
	except User.DoesNotExist:
		return HttpResponse("This user does not exist, proceed with user creation first ")
	
	try:
		cube = Cube.objects.get(id=cubeid)
	except Cube.DoesNotExist:
		return HttpResponse("This cube does not exist, proceed with cube creation first ")

	try:
		newuser = User.objects.get(id=newuserid)
	except User.DoesNotExist:
		return HttpResponse("This user with whom you are trying to share cube does not exist, proceed with user creation first ")

	if user.cubeid != cube.id:
		return HttpResponse("This cube does not exist for this user")
		
	user.cubeid = cube.id
	newuser.cubeid = cube.id

	cuber = {}
	cuber["cube-id"] = cube.id
	cuber["user-id"] = newuserid
	
	return HttpResponse(json.dumps(cuber))

#sharing a content with other user
def share_content(request,userid,contentid,newuserid):
	try:
		user = User.objects.get(id=userid)
	except User.DoesNotExist:
		return HttpResponse("This user does not exist, proceed with user creation first ")

	try:
		content = Content.objects.filter(id=contentid)
	except Content.DoesNotExist:
		return HttpResponse("This content does not exist, proceed with cube creation first ")

	try:
		user = User.objects.get(id=newuserid)																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																	
	except User.DoesNotExist:
		return HttpResponse("This user with whom you are trying to share cube does not exist, proceed with user creation first ")

	content_array = []
	for content_user in UserCont.objects.filter(Contentid = contentid):
		content_array.append(content_user.Useri)

	#if userid not in content_array:
		#return HttpResponse("Content not available for user %s " % str(userid) )

	if newuserid in content_array:
		return HttpResponse("The user you are trying to share your content already has been shared with")

	usercont = UserCont(Useri = newuserid,Contentid = contentid)
	usercont.save()

	contenter = {}
	contenter["content-id"] = contentid
	contenter["user-id"] = newuserid

	return HttpResponse(json.dumps(contenter))

#listing cube of a user
def cubes(request,userid):
	try:
		user = User.objects.get(id=userid)
	except User.DoesNotExist:
		return HttpResponse("This user does not exist, proceed with user creation first ")

	cubes = {}
	cubes["id"] = 1
	cubes["name"] = Cube.objects.get(id=user.cubeid).name
	cubes["user-id"] = user.id

	return HttpResponse(json.dumps(cubes))


#listing cube of a user
def contents(request,userid):
	try:
		user = User.objects.get(id=userid)
	except User.DoesNotExist:
		return HttpResponse("This user does not exist, proceed with user creation first ")


	contentlist = [user.Contentid for user in UserCont.objects.filter(Useri=userid)]
	count = 1
	content_list = []
	for i in contentlist:
		contents={}
		contents["id"] = count
		contents["link"] = Content.objects.get(id=i).link
		contents["user-id"] = userid
		content_list.append(contents)

	return HttpResponse(json.dumps(content_list))









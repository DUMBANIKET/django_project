
from django.shortcuts import render
from django.http import HttpResponse

posts=[
{
'image':'https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/refurb-iphone11-white-2019?wid=1144&hei=1144&fmt=jpeg&qlt=80&op_usm=0.5,0.5&.v=1611169090000',
'name':'Iphone 11',
'details':'The only phone with no updates',
'price':'$20,000',
},
{
'image':'https://d28i4xct2kl5lp.cloudfront.net/product_images/97757_2cc715ec-676c-4666-9790-035c6ddb21c7.jpg',
'name':'Airpods',
'details':'Pata nahi itna expensive kyu hai',
'price':'$10,000',
},


]


# Create your views here.
def home(request):
	context={'posts':posts}
	return render(request,'home/index.html',context)

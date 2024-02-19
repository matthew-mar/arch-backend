from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response, responses

from Arch_app.models import Period, Style, StylePhoto

from django.db.models import Q


@api_view()
def get_period(request):
    periods = {
        "periods": [],
    }

    for period in Period.objects.all():
        period_data = {
            "name": period.name,
            "from_year": period.from_year,
            "to_year": period.to_year,
            
        }

        periods["periods"].append(period_data)

    return Response(data=periods)


@api_view()
def get_periods_style(request, period_id):
    periods_styles = Style.objects.filter(period_id=period_id)
    styles = {
        "styles": [],
    }

    for style in periods_styles :
        style_data = {
            "name": style.name,
            "description": style.description,
            "parent_id": style.parent_id,
            "period_id": style.period_id.name
            
        }
        
        

        styles["styles"].append(style_data)

    return Response(data=styles)

def make_style_dict(style):
    return {
        "id":style.id,
        "name":style.name,
        "parent_id":style.parent_id,
        "period_id:":style.period_id.id,
        "time":style.time,
        "distinctive_features": style.distinctive_features,
        "basic_decorative_elements":style.basic_decorative_elements,
        "was_built":style.was_built,
        "example_name":style.example_name,
        "slug":style.slug

    }

def get_style_data(styles):
    styles_data =  {
        "styles":[],
    }
    for style in styles:
        style_info = make_style_dict(style)
        styles_data["styles"].append(style_info)

    return styles_data


@api_view()
def get_style(request, id):
    style = Style.objects.filter(id=id)
    if len(style) == 0:
        return Response(data=responses[404])
    else:    
        style_data = make_style_dict(style[0])
        return Response(data=style_data)

@api_view()   
def get_substyles(request, parent_id):
    substyles = Style.objects.filter(parent_id=parent_id)
    styles = get_style_data(substyles)
    return Response(data=styles)

@api_view(http_method_names=["POST"])
def search(request):
    data = request.data
    query = data["query"]
    results = Style.objects.filter(Q(description__contains=query) | Q(name__contains=query))
    styles = get_style_data(results)
    return Response(data=styles)

@api_view()
def style_photo(request, style_id):
    style_photos = StylePhoto.objects.filter(style_id = style_id)
    photos = {
        "links":[],
    }
    for photo in style_photos:
        photos["links"].append(photo.link_to_picture)
    return Response(data=photos)




@api_view()
def get_style_by_slug(request, slug):
    style = Style.objects.filter(slug=slug)
    if len(style) == 0:
        return Response(data=responses[404])
    else:    
        style_data = make_style_dict(style[0])
        return Response(data=style_data)

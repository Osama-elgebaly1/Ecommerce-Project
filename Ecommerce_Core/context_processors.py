from .models import Category

def categories_processors(request):
    """
    A context processor to make all product categories available 
    globally across all templates (e.g., for use in the navbar).

    Args:
        request (HttpRequest): The incoming HTTP request.

    Returns:
        dict: A dictionary containing all categories under the key 'categories'.
    """
    categories = Category.objects.all()
    return {'categories':categories}

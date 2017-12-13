import falcon
import images

def extract_project_id(req,resp,params):
    """Adds project_id' to the list of params for all responders.

    Meant to be used as a 'before' hook.
    """
    params['project_id']=req.get_header('X-PROJECT-ID')


api = application = falcon.API(before=[extract_project_id])
storage_path='/home/dy03/shijingxian/demo/exercises/look'
image_collection = images.Collection(storage_path)
image=images.Item(storage_path)
api.add_route('/images',image_collection)
api.add_route('/images/{name}',image)




#images= images.Resource('/home/dy03/Downloads/Goku.jpg')
#api.add_route('/images',images)


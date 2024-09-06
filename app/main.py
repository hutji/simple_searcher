import csv
import os

from aiohttp import web
from dotenv import load_dotenv

from app.services import delete_document, search_documents

load_dotenv()

routes = web.RouteTableDef()


def read_posts_csv(file_path):
    posts = []
    with open(file_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            posts.append(row)
    return posts


@routes.get("/search")
async def search(request):
    query = request.query.get("q")
    if not query:
        raise web.HTTPBadRequest(text='Query parameter "q" is required')

    documents = await search_documents(query)
    return web.json_response([doc.to_dict() for doc in documents])


@routes.delete("/documents/{id}")
async def delete(request):
    doc_id = int(request.match_info["id"])
    await delete_document(doc_id)
    return web.Response(status=204)


@routes.get("/posts")
async def get_posts(request):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "..", "data", "posts.csv")
    posts = read_posts_csv(file_path)
    return web.json_response(posts)


app = web.Application()
app.add_routes(routes)

if __name__ == "__main__":
    web.run_app(app)

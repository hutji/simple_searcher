from elasticsearch import AsyncElasticsearch
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.future import select
from sqlalchemy.orm import sessionmaker

from .models import Document
from .settings import DATABASE_URL, ELASTICSEARCH_URL

es = AsyncElasticsearch(ELASTICSEARCH_URL)
engine = create_async_engine(DATABASE_URL)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


async def search_documents(query: str):
    search_body = {"query": {"match": {"text": query}}, "size": 20}
    response = await es.search(index="documents", body=search_body)
    hits = response["hits"]["hits"]
    doc_ids = [hit["_source"]["id"] for hit in hits]

    async with async_session() as session:
        result = await session.execute(
            select(Document)
            .filter(Document.id.in_(doc_ids))
            .order_by(Document.created_date)
        )
        documents = result.scalars().all()

    return documents


async def delete_document(doc_id: int):
    await es.delete(index="documents", id=doc_id)
    async with async_session() as session:
        document = await session.get(Document, doc_id)
        if document:
            await session.delete(document)
            await session.commit()

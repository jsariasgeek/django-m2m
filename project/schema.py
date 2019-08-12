import graphene
from ubicaciones.schema import Mutation as ubicaciones_mutation
from ubicaciones.schema import Query as ubicaciones_query


class Mutation(ubicaciones_mutation):
    pass

class Query(ubicaciones_query):
    pass

schema = graphene.Schema(mutation=Mutation, query=Query)

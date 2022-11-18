from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

#SADeprecationWarning: The create_engine.convert_unicode parameter and corresponding dialect-level parameters are deprecated, and will be removed in a future release.  Modern DBAPIs support Python Unicode natively and this parameter is unnecessary.
# engine = create_engine('sqlite:///artigos.db', convert_unicode=True)
engine = create_engine('sqlite:///artigos.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Artigos(Base):
    __tablename__ = 'artigos'
    id = Column(Integer, primary_key=True)
    titulo = Column(String(40), index=True)
    conteudo = Column(String)
# criar coluna de imagem e data

    def __repr__(self):
        return '<Artigo {}>'.format(self.titulo)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

class Topicos(Base):
    __tablename__='topicos'
    id = Column(Integer, primary_key=True)
    titulo = Column(String(80))
    artigo_id = Column(Integer, ForeignKey('artigos.id'))
    artigo = relationship("Artigos")

    def __repr__(self):
        return '<Topicos {}>'.format(self.titulo)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

# def save(self):
# db_session.add(self)
# db_session.commit()

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()
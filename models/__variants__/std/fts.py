#
# Automatically generated from Gel schema.
#
# Do not edit directly as re-generating this file will overwrite any changes.
#

from __future__ import annotations

from gel.models.pydantic import AnyEnum, BaseScalar, GelTypeMeta, SchemaPath

from typing import TYPE_CHECKING
from uuid import UUID

if TYPE_CHECKING:

    from typing import ClassVar


class ElasticLanguage(AnyEnum):
    """
    Languages supported by ElasticSearch. Names are ISO 639-3 language
    identifiers or EdgeDB language identifers.
    """
    ara = 'ara'
    bul = 'bul'
    cat = 'cat'
    ces = 'ces'
    ckb = 'ckb'
    dan = 'dan'
    deu = 'deu'
    ell = 'ell'
    eng = 'eng'
    eus = 'eus'
    fas = 'fas'
    fin = 'fin'
    fra = 'fra'
    gle = 'gle'
    glg = 'glg'
    hin = 'hin'
    hun = 'hun'
    hye = 'hye'
    ind = 'ind'
    ita = 'ita'
    lav = 'lav'
    nld = 'nld'
    nor = 'nor'
    por = 'por'
    ron = 'ron'
    rus = 'rus'
    spa = 'spa'
    swe = 'swe'
    tha = 'tha'
    tur = 'tur'
    zho = 'zho'
    edb_Brazilian = 'edb_Brazilian'
    edb_ChineseJapaneseKorean = 'edb_ChineseJapaneseKorean'


class Language(AnyEnum):
    """
    Languages supported by PostgreSQL FTS, ElasticSearch and Apache
    Lucene. Names are ISO 639-3 language identifiers.
    """
    ara = 'ara'
    hye = 'hye'
    eus = 'eus'
    cat = 'cat'
    dan = 'dan'
    nld = 'nld'
    eng = 'eng'
    fin = 'fin'
    fra = 'fra'
    deu = 'deu'
    ell = 'ell'
    hin = 'hin'
    hun = 'hun'
    ind = 'ind'
    gle = 'gle'
    ita = 'ita'
    nor = 'nor'
    por = 'por'
    ron = 'ron'
    rus = 'rus'
    spa = 'spa'
    swe = 'swe'
    tur = 'tur'


class LuceneLanguage(AnyEnum):
    """
    Languages supported by Apache Lucene. Names are ISO 639-3 language
    identifiers or EdgeDB language identifers.
    """
    ara = 'ara'
    ben = 'ben'
    bul = 'bul'
    cat = 'cat'
    ces = 'ces'
    ckb = 'ckb'
    dan = 'dan'
    deu = 'deu'
    ell = 'ell'
    eng = 'eng'
    est = 'est'
    eus = 'eus'
    fas = 'fas'
    fin = 'fin'
    fra = 'fra'
    gle = 'gle'
    glg = 'glg'
    hin = 'hin'
    hun = 'hun'
    hye = 'hye'
    ind = 'ind'
    ita = 'ita'
    lav = 'lav'
    lit = 'lit'
    nld = 'nld'
    nor = 'nor'
    por = 'por'
    ron = 'ron'
    rus = 'rus'
    spa = 'spa'
    srp = 'srp'
    swe = 'swe'
    tha = 'tha'
    tur = 'tur'
    edb_Brazilian = 'edb_Brazilian'
    edb_ChineseJapaneseKorean = 'edb_ChineseJapaneseKorean'
    edb_Indian = 'edb_Indian'


class PGLanguage(AnyEnum):
    """
    Languages supported by PostgreSQL FTS. Names are ISO 639-3 language
    identifiers or Postgres regconfig names prefixed with `xxx_`.
    """
    xxx_simple = 'xxx_simple'
    ara = 'ara'
    hye = 'hye'
    eus = 'eus'
    cat = 'cat'
    dan = 'dan'
    nld = 'nld'
    eng = 'eng'
    fin = 'fin'
    fra = 'fra'
    deu = 'deu'
    ell = 'ell'
    hin = 'hin'
    hun = 'hun'
    ind = 'ind'
    gle = 'gle'
    ita = 'ita'
    lit = 'lit'
    npi = 'npi'
    nor = 'nor'
    por = 'por'
    ron = 'ron'
    rus = 'rus'
    srp = 'srp'
    spa = 'spa'
    swe = 'swe'
    tam = 'tam'
    tur = 'tur'
    yid = 'yid'


class Weight(AnyEnum):
    """
    Weight category. Weight values for each category can be provided in
    std::fts::search.
    """
    A = 'A'
    B = 'B'
    C = 'C'
    D = 'D'



class __document_meta__(GelTypeMeta):
    pass
if TYPE_CHECKING:
    class document(BaseScalar, metaclass=__document_meta__):
        class __gel_reflection__:
            id = UUID(int=39063313325870458915035536806779586498)
            name = SchemaPath('std', 'fts', 'document')

if not TYPE_CHECKING:
    class document(BaseScalar):
        __gel_type_class__: ClassVar[type] = __document_meta__

        class __gel_reflection__:
            id = UUID(int=39063313325870458915035536806779586498)
            name = SchemaPath('std', 'fts', 'document')



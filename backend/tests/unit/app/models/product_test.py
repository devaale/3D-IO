from app.models.product import Product, ProductCreate, ProductDelete, ProductUpdate


def test_product_from_orm_create():
    expected = ProductCreate()
    result = Product.from_orm(expected)
    assert result.model == expected.model


def test_product_from_orm_delete():
    expected = ProductDelete()
    result = Product.from_orm(expected)
    assert result.model == expected.model


def test_product_from_orm_update():
    expected = ProductUpdate()
    result = Product.from_orm(expected)
    assert result.model == expected.model


def test_product_from_orm_read():
    expected = ProductCreate()
    result = Product.from_orm(expected)
    assert result.model == expected.model

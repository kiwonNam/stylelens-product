from bson.objectid import ObjectId
from stylelens_product.database import DataBase

class Products(DataBase):
  def __init__(self):
    super(Products, self).__init__()
    self.products = self.db.products

  def add_product(self, product):
    object_id = None
    query = {"host_code": product['host_code'], "product_no": product["product_no"]}
    try:
      r = self.products.update_one(query,
                                  {"$set": product},
                                  upsert=True)
    except Exception as e:
      print(e)

    if 'upserted' in r.raw_result:
      product_id = str(r.raw_result['upserted'])

    return product_id

  def get_products_by_hostcode_and_version_id(self,
                                              host_code, version_id,
                                              is_processed=False,
                                              is_classified=False,
                                              offset=0, limit=100):
    query = {}
    query['host_code'] = host_code
    query['version_id'] = version_id
    query['is_processed'] = is_processed
    query['is_classified'] = is_classified
    try:
      r = self.products.find(query).skip(offset).limit(limit)
    except Exception as e:
      print(e)

    return list(r)

  def get_products_by_version_id(self,
                                  version_id,
                                  is_processed=False,
                                  is_classified=False,
                                  offset=0, limit=100):
    query = {}
    query['version_id'] = version_id
    query['is_processed'] = is_processed

    if is_classified is False:
      query['$or'] = [{'is_classified':False}, {'is_classified':None}]
    else:
      query['is_classified'] = True

    try:
      r = self.products.find(query).skip(offset).limit(limit)
    except Exception as e:
      print(e)

    return list(r)

  def get_size_not_classified(self, version_id):
    query = {}
    query['version_id'] = version_id
    query['is_classified'] = False

    try:
      count = self.products.find(query).count()
    except Exception as e:
      print(e)

    return count

  def update_product_by_id(self, product_id, product):
    try:
      r = self.products.update_one({"_id": ObjectId(product_id)},
                                  {"$set": product})
    except Exception as e:
      print(e)

    return r.modified_count

  def update_product_by_hostcode_and_productno(self, product):
    query = {"host_code": product['host_code'], "product_no": product['product_no']}
    try:
      r = self.products.update_one(query,
                                  {"$set": product},
                                  upsert=True)
    except Exception as e:
      print(e)

    return r.raw_result

  def delete_products_by_hostcode_and_version_id(self, host_code, version_id, except_version=True):
    if except_version == True:
      query = {"host_code": host_code, "version_id": version_id}
    else:
      query = {"host_code": host_code, "version_id": {"$ne": version_id}}

    try:
      r = self.products.delete_many(query)
    except Exception as e:
      print(e)

    return r.raw_result

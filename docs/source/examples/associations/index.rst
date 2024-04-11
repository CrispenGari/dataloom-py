Associations
++++++++++++

In dataloom you can create association using the ``foreign-keys`` column during model creation. You just have to specify a single model to have a relationship with another model using the ``ForeignKeyColum``. Just by doing that ``dataloom`` will be able to learn bidirectional relationship between your models. Let's have a look at the following examples:

#. `One to One Association <one_to_one.html>`_ 
#. `One to Many Association <one_to_n.html>`_ 
#. `Many to One Association <n_to_one.html>`_ 
#. `What about bidirectional queries? <bi_directional.html>`_ 
#. `Self Association <self_relations.html>`_ 
#. `Many to Many Association <n_to_n.html>`_ 



.. toctree::
   :maxdepth: 2
   :hidden:

   one_to_one
   one_to_n
   n_to_one
   bi_directional
   self_relations
   n_to_n
   
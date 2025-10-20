textx generate barebone.tx --target dot
dot -Tpng -O barebone.dot

textx generate Test1.bb --grammar barebone.tx --target dot
dot -Tpng -O Test1.dot

textx generate Test2.bb --grammar barebone.tx --target dot
dot -Tpng -O Test2.dot

textx generate Test3.bb --grammar barebone.tx --target dot
dot -Tpng -O Test3.dot

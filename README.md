# مشروع تحليل بيانات سيارات الأجرة في نيويورك باستخدام PySpark

هذا المشروع يوضح كيفية استخدام Apache PySpark لتحليل بيانات رحلات سيارات الأجرة الصفراء في مدينة نيويورك لشهر مارس 2016. يتضمن المشروع أمثلة على عمليات DataFrame الأساسية، معالجة القيم المفقودة، عمليات التصفية، وظائف GroupBy والتجميع، وتطبيق نماذج التعلم الآلي مثل الانحدار الخطي.

## محتويات المشروع

*   `data/`: يحتوي على ملف البيانات `yellow_tripdata_2016-03.csv`.
*   `notebooks/`: يحتوي على دفاتر ملاحظات Jupyter التي توضح خطوات التحليل المختلفة:
    *   `01_data_exploration.ipynb`: استكشاف البيانات الأساسية وعرض المخطط والصفوف الأولى.
    *   `02_dataframe_operations.ipynb`: عمليات DataFrame مثل اختيار الأعمدة، إضافة/حذف/إعادة تسمية الأعمدة.
    *   `03_handling_missing_values.ipynb`: طرق معالجة القيم المفقودة (الإسقاط والملء).
    *   `04_filter_operations.ipynb`: عمليات التصفية على DataFrame باستخدام شروط مختلفة.
    *   `05_groupby_aggregate.ipynb`: استخدام وظائف GroupBy والتجميع لإجراء تحليلات إحصائية.
    *   `06_linear_regression.ipynb`: تطبيق نموذج الانحدار الخطي للتنبؤ بـ `fare_amount`.
    *   `07_pyspark_ml_examples.ipynb`: أمثلة متقدمة للتعلم الآلي باستخدام Random Forest Regressor.
*   `scripts/`: يحتوي على ملفات Python القابلة للتنفيذ:
    *   `main.py`: مثال بسيط لإنشاء SparkSession وتحميل البيانات.

## إعداد البيئة

لإعداد بيئة التطوير وتشغيل المشروع، اتبع الخطوات التالية:

1.  **استنساخ المستودع (Clone the repository):**

    ```bash
    git clone <رابط المستودع الخاص بك>
    cd pyspark_taxi_project
    ```

2.  **إنشاء بيئة افتراضية وتثبيت التبعيات:**

    ```bash
    python3.11 -m venv venv
    source venv/bin/activate
    pip install pyspark jupyter
    ```

3.  **تنزيل مجموعة البيانات:**

    ملف البيانات `yellow_tripdata_2016-03.csv` كبير الحجم (حوالي 1.8 جيجابايت). تأكد من توفر مساحة كافية على القرص. يمكنك تنزيله يدويًا ووضعه في مجلد `data/`، أو استخدام الأمر التالي:

    ```bash
    wget -O data/yellow_tripdata_2016-03.csv https://storage.googleapis.com/anaconda-public-data/nyc-taxi/csv/2016/yellow_tripdata_2016-03.csv
    ```

## تشغيل دفاتر الملاحظات (Jupyter Notebooks)

بعد إعداد البيئة وتنزيل البيانات، يمكنك تشغيل دفاتر الملاحظات:

1.  **تفعيل البيئة الافتراضية:**

    ```bash
    source venv/bin/activate
    ```

2.  **بدء Jupyter Notebook:**

    ```bash
    jupyter notebook
    ```

    سيتم فتح متصفح الويب الخاص بك مع واجهة Jupyter. انتقل إلى مجلد `notebooks/` وافتح أي دفتر ملاحظات لتشغيله.

## تشغيل السكريبتات (Scripts)

يمكنك تشغيل السكريبتات الموجودة في مجلد `scripts/` باستخدام Python:

1.  **تفعيل البيئة الافتراضية:**

    ```bash
    source venv/bin/activate
    ```

2.  **تشغيل السكريبت:**

    ```bash
    python scripts/main.py
    ```

## المساهمة

نرحب بالمساهمات في هذا المشروع. يرجى فتح مشكلة (issue) أو إرسال طلب سحب (pull request).

## الترخيص

هذا المشروع مرخص بموجب ترخيص MIT. انظر ملف `LICENSE` لمزيد من التفاصيل.

Title: Пагинация в Oracle
Date: 2013-05-17 1:00
Category: Blog
Tags: pl/sql, oracle, pagination, пагинация
Slug: oracle-pagination
Author: Sergey Tsaplin
Summary: Short version for index and feeds
Lang: ru

Как известно, БД от Oracle не поддерживает инструкцию ``LIMIT`` в SQL-запросах. Поэтому на первых порах часто возникают вопросы, о том как реализовать пагинацию в Oracle. Тут на самом деле все просто. Достаточно использовать ``rownum``, например вот так:

    :::sql
    select *
    from some_table
    where <some_conditions>
       and rownum >= 1
       and rownum < 20

Казалось бы ВОТ ОНО. Но не тут то было. Как только возникает потребность реализовать пагинацию над некой агрегированной выборкой (выборка с использованием групповых функций), приходится выполнить ряд дополнительных телодвижений:

    :::sql
    select tmp.*
    from
      (select field1,
              count(field2) field2_cnt
              sum(field3) field3_sum
       from some_table
       where <some_conditions>
       group by field1) tmp
    where rownum >= 1
      and rownum < 20

Что здесь происходит? Здесь сначала делается выборка по полям, удовлетворяющим условиям, выполняются групповые операции над ними, затем отсечку по rownum делаем уже над сгруппированными данными, таким образом пагинация работает, как и ожидалось. Вот такой вот небольшой хинт. Ну и всё это можно обернуть в некую хранимую функцию на pl/sql:

    :::plpgsql
    function get_padgination_cursor(page in integer := 1) return sys_ref_cursor as
      cr sys_ref_cursor;
      records_per_page integer := 20;
      start_limit integer := records_per_page * (page - 1) + 1;
      stop_limit integer := start_limit + records_per_page;
    begin
      open cr for
        select tmp.*
        from
          (select field1,
                  count(field2) field2_cnt
                  sum(field3) field3_sum
           from some_table
           where <some_conditions>
           group by field1) tmp
        where rownum >= start_limit
          and rownum < stop_limit;

      return cr;
    end;
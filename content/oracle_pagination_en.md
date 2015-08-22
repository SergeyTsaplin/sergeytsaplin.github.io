Title: Pagination in Oracle
Date: 2013-05-17 1:00
Category: Blog
Tags: pl/sql, oracle, pagination
Slug: oracle-pagination
Author: Sergey Tsaplin
Summary: Short version for index and feeds
Lang: en
Status: draft

As you know Oracle Database doesn't support the ``LIMIT`` instruction in SQL queries. So you can stacked with this problem. But there is a simple way to do it. It enough to use ``rownum`` field:

    :::sql
    select *
    from some_table
    where <some_conditions>
       and rownum >= 1
       and rownum < 20

It seems like WIN. But it is not absolutely. If we want to paginate some aggregated data (queries uses aggregating functions), we have to do some extra actions:

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

What's this code doing? First of all we get all necessary fields which satisfied with conditions, then do aggregation operations on them. And finally cut aggregated data by ``rownum``, so pagination is done. Also you can wrap it all by `pl/sql` stored function:

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
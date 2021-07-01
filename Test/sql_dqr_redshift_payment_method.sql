"[{'sql_': ""update\n  cds.order_total_modifier\nset\n  cds_update_time = sysdate,\n  payment_method = regexp_replace(\n    payment_method,\n    '(.*[Cc]ard( [Pp]ayment [Ww]ith)?)[^a-z][Xx*-]*[0-9]{4,}([ -][0-9]{4,})*(.*)',\n    '$1 ^Payment^$4'\n  )\nwhere\n  payment_method ~ '.*[Cc]ard( [Pp]ayment [Ww]ith)?[^a-z][Xx*-]*[0-9]{4,}.*'""}]"

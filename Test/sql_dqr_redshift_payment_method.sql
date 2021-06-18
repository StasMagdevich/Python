update
  cds.order_total_modifier
set
  cds_update_time = sysdate,
  payment_method = regexp_replace(
    payment_method,
    '(.*[Cc]ard( [Pp]ayment [Ww]ith)?)[^a-z][Xx*-]*[0-9]{4,}([ -][0-9]{4,})*(.*)',
    '$1 ^Payment^$4'
  )
where
  payment_method ~ '.*[Cc]ard( [Pp]ayment [Ww]ith)?[^a-z][Xx*-]*[0-9]{4,}.*'
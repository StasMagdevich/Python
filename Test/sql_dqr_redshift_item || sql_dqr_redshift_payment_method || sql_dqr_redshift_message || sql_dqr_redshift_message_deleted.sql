/*lz_pii_transaction_id-message-redshift*/
update
  cds.item
set
  description = REGEXP_REPLACE (
    description,
    '(.*)(transaction id: .*)',
    '$1transaction id: ^transaction_id^)'
  ),
  cds_update_time = sysdate
WHERE
  description ILIKE '%(transaction id:%'

; 

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
  payment_method ~ '.*[Cc]ard( [Pp]ayment [Ww]ith)?[^a-z][Xx*-]*[0-9]{4,}.*'; 

 update baikal.message
set subject = 
REGEXP_REPLACE(subject, '(.*[Pp]ayment [Pp]rocessed for [Aa]ccount [Ee]nding in).*', '\\1 ^account_id^'), cds_update_time = sysdate
WHERE 
subject ILIKE '%payment processed for account ending in%'; 

 update
  cds.message_deleted
set
  subject = REGEXP_REPLACE(
    subject,
    '(.*[Pp]ayment [Pp]rocessed for [Aa]ccount [Ee]nding in).*',
    '\\1 ^account_id^'
  ),
  cds_update_time = sysdate
WHERE
  subject ILIKE '%payment processed for account ending in%'
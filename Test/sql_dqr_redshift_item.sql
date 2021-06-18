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


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
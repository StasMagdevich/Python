/*lz_pii_transaction_id-message-redshift*/\\nupdate\\n  cds.item\\nset\\n  description = REGEXP_REPLACE (\\n    description\,\\n    '(.*)(transaction id: .*)'\,\\n    '$1transaction id: ^transaction_id^)'\\n  )\,\\n  cds_update_time = sysdate\\nWHERE\\n  description ILIKE '%(transaction id:%'\\n\\n

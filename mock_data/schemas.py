from google.cloud import bigquery

# card_schema = {
#     "id_cartao": "STRING",
#     "id_produto_cartao": "STRING",
#     "num_cartao": "STRING",
#     "num_seq_via_cartao": "STRING",
#     "id_conta": "STRING",
#     "num_cpf_cliente": "STRING",
#     "cod_tip_portador": "STRING",
#     "num_bin": "STRING",
#     "cod_loja_emis_cartao": "STRING",
#     "id_cliente_so": "STRING",
#     "dth_emis_cartao": "TIMESTAMP",
#     "dth_embs_cartao": "TIMESTAMP",
#     "dth_valid_cartao": "TIMESTAMP",
#     "dth_desbloqueio": "TIMESTAMP",
#     "cod_sit_cartao": "STRING",
#     "des_sit_cartao": "STRING",
#     "dth_sit_cartao": "TIMESTAMP",
#     "cod_estagio_cartao": "STRING",
#     "des_estagio_cartao": "STRING",
#     "dth_estagio_cartao": "TIMESTAMP",
#     "flg_embs_loja": "STRING",
#     "flg_cartao_cancelado": "STRING",
#     "flg_cartao_provisorio": "STRING",
#     "flg_conta_cancelada": "STRING",
#     "dth_ult_atu_so": "TIMESTAMP",
#     "num_seq_ult_alteracao": "STRING",
#     "dth_inclusao_reg": "TIMESTAMP",
#     "pt_nomeplastico": "STRING",
#     "ca_arquivolote": "STRING",
#     "ca_id_imagem": "STRING",
#     "bc_responsavel": "STRING",
#     "ca_codigocancelamento": "STRING",
#     "ca_flaggeracartasenha": "STRING",
#     "pt_id_imagem": "STRING",
# }

bigquery_schema_person = [
    bigquery.SchemaField("id_pessoa", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("nome", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("cpf", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("data_nascimento", "TIMESTAMP", mode="REQUIRED"),
    bigquery.SchemaField("sexo", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("estado_civil", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("nacionalidade", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("endereco", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("telefone", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("email", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("data_criacao_registro", "TIMESTAMP", mode="REQUIRED"),
]

bigquery_schema_account = [
    bigquery.SchemaField("id_conta", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("num_conta", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("tipo_conta", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("status_conta", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("data_abertura", "TIMESTAMP", mode="REQUIRED"),
    bigquery.SchemaField("data_encerramento", "TIMESTAMP", mode="NULLABLE"),
    bigquery.SchemaField("saldo_conta", "FLOAT", mode="REQUIRED"),
    bigquery.SchemaField("id_pessoa", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("data_ultima_movimentacao", "TIMESTAMP", mode="NULLABLE"),
]

bigquery_schema_card = [
    bigquery.SchemaField("id_cartao", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("id_produto_cartao", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("num_cartao", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("num_seq_via_cartao", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("id_conta", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("num_cpf_cliente", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("cod_tip_portador", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("num_bin", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("cod_loja_emis_cartao", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("id_cliente_so", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("dth_emis_cartao", "TIMESTAMP", mode="REQUIRED"),
    bigquery.SchemaField("dth_embs_cartao", "TIMESTAMP", mode="NULLABLE"),
    bigquery.SchemaField("dth_valid_cartao", "TIMESTAMP", mode="REQUIRED"),
    bigquery.SchemaField("dth_desbloqueio", "TIMESTAMP", mode="NULLABLE"),
    bigquery.SchemaField("cod_sit_cartao", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("des_sit_cartao", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("dth_sit_cartao", "TIMESTAMP", mode="REQUIRED"),
    bigquery.SchemaField("cod_estagio_cartao", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("des_estagio_cartao", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("dth_estagio_cartao", "TIMESTAMP", mode="REQUIRED"),
    bigquery.SchemaField("flg_embs_loja", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("flg_cartao_cancelado", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("flg_cartao_provisorio", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("flg_conta_cancelada", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("dth_ult_atu_so", "TIMESTAMP", mode="REQUIRED"),
    bigquery.SchemaField("num_seq_ult_alteracao", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("dth_inclusao_reg", "TIMESTAMP", mode="REQUIRED"),
    bigquery.SchemaField("pt_nomeplastico", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("ca_arquivolote", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("ca_id_imagem", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("bc_responsavel", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("ca_codigocancelamento", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("ca_flaggeracartasenha", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("pt_id_imagem", "STRING", mode="NULLABLE"),
]
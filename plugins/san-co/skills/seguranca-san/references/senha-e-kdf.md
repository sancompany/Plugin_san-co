# Senha e derivação de chave — o que decidir antes da primeira linha de autenticação

A Lei 3 dá a ordem de preferência: **Argon2id**; **scrypt** quando Argon2id não estiver disponível; PBKDF2 só sob exigência de FIPS-140; bcrypt apenas em sistema legado (trunca a senha em 72 bytes). Este arquivo é o que vem depois da escolha — os custos que precisam ser assumidos de propósito, não descobertos depois. Sete das lições do catálogo (10, 11, 12, 13, 21, 26, 29) nasceram aqui.

## Biblioteca ou primitiva crua

`crypto.scrypt` do Node é scrypt de verdade (RFC 7914), sem dependência nativa e sem superfície de supply-chain. Usá-lo cru compensa **só se todos os pontos abaixo forem implementados e testados**. Não sendo, a biblioteca com Argon2id é a escolha mais segura — e antes de remover uma dependência para reimplementar à mão, listar o que ela fazia além da função óbvia (lição nº 11): salt por senha, formato de armazenamento, parâmetros embutidos, comparação em tempo constante.

**No navegador**, derivando chave de cofre, a alternativa ao Argon2id é **PBKDF2-SHA256 com 310.000 ou mais iterações**, e não scrypt — é o único dos três nativo no Web Crypto, e trazer implementação própria de KDF para o front-end é pior que o parâmetro inferior.

## Os custos de usar scrypt cru

**O parâmetro padrão não serve, e o mínimo é piso, não alvo.** O padrão do Node é N=2^14; o piso recomendado é **N=2^17, r=8, p=1**, e abaixo dele nunca (lição nº 10). Acima, calibrar: o maior custo que a máquina de produção absorve com os logins simultâneos que existem, mirando 0,5 a 1 segundo por hash **medido no servidor real**. Número copiado de artigo não é calibração.

**Custo alto é memória, e memória vira negação de serviço.** scrypt consome cerca de `128 × N × r` bytes **por hash em andamento** — a 2^17 com r=8, ~128 MiB cada. Dez logins simultâneos são ~1,3 GB. Isso é limite assumido e vai para o `CONSTRAINTS.md` (Lei 7).

**O `maxmem` do Node barra isso por padrão** — 32 MiB, então a 2^17 a chamada **lança exceção** se `maxmem` não for aumentado explicitamente. Falha fechado, o que é bom; mas quem não souber baixa o N até "funcionar", e a segurança cai sem ninguém perceber (lição nº 13). **Aumentar o limite, nunca reduzir a segurança.**

**Derivar de forma assíncrona, sempre.** A 2^17 a versão síncrona segura o event loop por quase um segundo — e em Node isso atinge **toda requisição em voo**, inclusive confirmação de pagamento sem relação nenhuma com o login. `crypto.scrypt`, nunca `scryptSync`, em qualquer caminho servido por requisição (lição nº 12).

**Teto de simultaneidade, não só de taxa.** Limite por minuto não impede duas derivações ao mesmo tempo, e duas a 2^17 são ~256 MiB de uma vez — foi assim que um serviço caiu. A pergunta é *quantas destas cabem juntas nesta instância?*, e a resposta vira limite no código (lição nº 21).

**Sem biblioteca, a responsabilidade é sua.** Gerar salt aleatório por senha; guardar salt e parâmetros junto do hash, para verificar depois e migrar parâmetros no futuro; comparar em tempo constante com `timingSafeEqual`.

**Comparação segura cumpre a promessa sozinha.** Envolvendo `timingSafeEqual` num utilitário, a proteção contra entrada ausente é dele, não de quem chama — normalizar com valor padrão vazio faz dois vazios baterem, e "credencial ausente" vira "credencial confere" (lição nº 29).

**Segredo com caractere especial de shell** — `$`, crase, contrabarra, aspas — é guardado codificado em base64 ou hex e decodificado no processo. Várias plataformas expandem shell no valor da variável e apagam parte do segredo em silêncio; o formato padrão de hash de senha tem cifrão por construção, então a colisão é previsível (lição nº 26). Rota de segurança que responde **rápido demais** é sinal tão forte quanto rota que responde errado.

## O que registrar

No código, os parâmetros escritos explicitamente com a data e a fonte da recomendação — nunca implícitos no padrão da biblioteca. No `CONSTRAINTS.md`, o custo de memória por hash e o teto de simultaneidade, como limite declarado.

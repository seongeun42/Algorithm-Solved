SELECT count(*) COUNT
FROM ECOLI_DATA
WHERE bin(GENOTYPE) like "%01"
    or bin(GENOTYPE) like "1"
    or bin(GENOTYPE) like "%10_"
for filename in easy/*.cnf; do
  ./run < filename > stats/filename
done

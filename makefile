all:RungeKuttaEdoSolution.txt  period_amplitude.txt

RungeKuttaEdoSolution.txt: a.out
	./a.out
a.out: Tarea7.c
	cc Tarea7.c -lm 
period_amplitude.txt: tarea7.py
	python tarea7.py


clean:
	rm -f *.out 
	rm -f *.txt 
	rm -f *.png 
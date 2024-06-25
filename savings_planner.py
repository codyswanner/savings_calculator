from math import sqrt


def calculate_years(yearly_savings: int, total_savings: int) -> int:
	# Yep, it's a weird one.  Trust the math.
	years: int = -6+sqrt(36+(12*total_savings/yearly_savings))
	return years


def calculate_yearly_savings(years: int, total_savings: int) -> int:
	yearly_savings: int = 12*total_savings / (years**2 + 12*years)
	return yearly_savings


def calculate_total_savings(years: int, yearly_savings: int) -> int:
	total_savings: int = yearly_savings*(years**2)/12 + yearly_savings*years
	return total_savings


def main() -> None:
	years: int
	yearly_savings: int
	total_savings: int

	mode: string = input(
	"Which would you like to calculate? \n \
	(1) years to save \n \
	(2) amount to save per year \n \
	(3) total saved amount \n \
	Please use numbers only: "
	)

	cont: bool = True
	match mode:
		case "1":
			while cont:
				try:
					yearly_savings = int(input("How much will you save per year? "))
					total_savings = int(input("What is your total savings goal? "))
					years = calculate_years(yearly_savings, total_savings)
					cont = False
				except ValueError:
					print("Please use numbers only.")
		case "2":
			while cont:
				try:
					years = int(input("For how many years will you save? "))
					total_savings = int(input("What is your total savings goal? "))
					yearly_savings = calculate_yearly_savings(years, total_savings)
					cont = False
				except ValueError:
					print("Please use numbers only.")
		case "3":
			while cont:
				try:
					years = int(input("For how many years will you save? "))
					yearly_savings = int(input("How much will you save per year? "))
					total_savings = calculate_total_savings(years, yearly_savings)
					cont = False
				except ValueError:
					print("Please use numbers only.")

	print("Final numbers:")
	print(f"Years to save: {years:,.2f}")
	print(f"Amount per year: {yearly_savings:,.2f}")
	print(f"Total amount: {total_savings:,.2f}")
	print(f"You'll need to save {yearly_savings/12} per month to meet this target.")

if __name__ == "__main__":
	while True:
		main()
		repeat: str = input("Calculate again? (y/n): ")
		if repeat.lower() != "y":
			break


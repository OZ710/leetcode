class Solution {
public:


	string numberToWords(int num) {
		string out = "";
		string one[] = { "","One","Two","Three","Four","Five","Six","Seven","Eight" ,"Nine" };
		string teen[] = { "","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen" };
		string ten[] = { "","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety" };
		int n;
		if (num == 0)
			out = "Zero";
		n = num / 1000000000;
		if (n > 0)
		{
			out = out + one[n] + " Billion";
			if ((num / 1000) % 1000 > 0 || num % 1000 > 0 || (num / 1000000) % 1000 > 0)
				out = out + " ";
		}

		n = (num / 1000000) % 1000;
		if (n > 0)
		{
			if (n >= 100)
				out = out + one[(n / 100)] + " Hundred";
			if (n % 100 != 0 && n > 100)
				out = out + " ";
			n = n % 100;
			if (n > 10 && n < 20)
				out = out + teen[(n % 10)];
			else if (n < 10)
			{
				out = out + one[n];
			}
			else
			{
				if (n == 10)
					out = out + "Ten";
				else if (n % 10 == 0)
					out = out + ten[n / 10];
				else
					out = out + ten[n / 10] + " " + one[n % 10];

			}
			out = out + " Million";
			if ((num / 1000) % 1000 > 0 || num % 1000 > 0)
				out = out + " ";
		}
		n = (num / 1000) % 1000;
		if (n > 0)
		{
			if (n >= 100)
				out = out + one[(n / 100)] + " Hundred";
			if (n % 100 != 0 && n > 100)
				out = out + " ";
			n = n % 100;
			if (n > 10 && n < 20)
				out = out + teen[(n % 10)];
			else if (n < 10)
			{
				out = out + one[n];
			}
			else
			{
				if (n == 10)
					out = out + "Ten";
				else if (n % 10 == 0)
					out = out + ten[n / 10];
				else
					out = out + ten[n / 10] + " " + one[n % 10];

			}

			out = out + " Thousand";
			if (num % 1000 > 0)
				out = out + " ";
		}

		n = num % 1000;
		if (n > 0)
		{
			if (n >= 100)
				out = out + one[(n / 100)] + " Hundred";
			if (n % 100 != 0 && n > 100)
				out = out + " ";
			n = n % 100;
			if (n > 10 && n < 20)
				out = out + teen[(n % 10)];
			else if (n < 10)
			{
				out = out + one[n];
			}
			else
			{
				if (n == 10)
					out = out + "Ten";
				else if (n % 10 == 0)
					out = out + ten[n / 10];
				else
					out = out + ten[n / 10] + " " + one[n % 10];

			}

		}
		return out;
	}
};
/*
Write a code to get the input in the given format and print the output in the given format.

Input Description:
First-line indicates two integers which are the size of array and 'K' value. Second-line indicates an integer contains elements of an array.

Output Description:
Print the taken input in the same format.

Sample Input :
5 3
1 2 3 4 5
Sample Output :
5 3
1 2 3 4 5
*/

import java.util.Scanner;
class Main{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		//inputs
		int n,k;
		n=sc.nextInt();
		k=sc.nextInt();
		//array
		int[] numArr= new int[n];
		for(int i=0; i<n; i++){
			numArr[i]=sc.nextInt();
		}
		int last= numArr[n-1];
		System.out.println(n+ " " +k);
		for(int i=0;i<n;i++){
			if(numArr[i]==last){
				System.out.print(numArr[i]);
				break;
			}
			System.out.print(numArr[i] + " ");
		}
		sc.close();
	}
}
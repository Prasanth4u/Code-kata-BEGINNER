"""
Ramesh is searching a solution to problem posted. The statement is as follows

Print the maximum sum produced by increasing subarray. Ramesh is very confused to see the question,Help him.

Input Description:
You are given a number ‘n’,Then next line contains n space separated numbers.

Output Description:
Maximum sum value produced by the increasing sub array of size 'n'

Sample Input :
6
2 1 4 7 3 6
Sample Output :
12
"""
import java.util.Scanner;
class Main {  
  public static void main(String args[]) {
	  	  
	  Scanner sc = new Scanner(System.in);
	  int n= sc.nextInt();
	  int[] arr=new int[n];
	  
	  for(int i= 0 ; i<n; i++){
		  arr[i]=sc.nextInt();
	  }
	  
	  int cur_sum=arr[0];
	  int max_sum=arr[0];
	  
	  for(int j=1; j<n; j++){
		  if(arr[j-1] < arr[j]){
			  cur_sum += arr[j];
			  max_sum=Math.max(max_sum,cur_sum);			  
		  }
		  else{
			  max_sum=Math.max(max_sum,cur_sum);
			  cur_sum=arr[j];
		  }
	  }
	  System.out.print(max_sum);
  } 
}
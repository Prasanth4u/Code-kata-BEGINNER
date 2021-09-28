"""
Write a program to rotate the given string by the given number of times.

Input Description:
String, rotation times

Output Description:
print the Rotated string

Sample Input :
hello 3
Sample Output :
llohe
"""
//Program
import java.util.Scanner;
class Main {  
  public static void main(String args[]) {
	  	  
	  Scanner sc = new Scanner(System.in);
	  String str=sc.nextLine();
	  int n= sc.nextInt();
      String res= str.substring(n-1)+str.substring(0,n-1);
	  System.out.println(res);
	  
  } 
}
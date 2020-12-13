import java.util.Scanner;


public class main {
	
	public static void main(String[] args){
		
		
		int basamak_sayisi=0,sayi,toplam=0,basamak_toplam=1,temp1,temp2,x;
		
		Scanner scan = new Scanner(System.in);
		
		System.out.println("sayiyi giriniz:");
		
		sayi = scan.nextInt();
		temp1 = sayi;
		temp2 = sayi;
		
		while(temp1>0){
			temp1 = temp1/10;
			basamak_sayisi++;
		}
		
		while(temp2>0){ // 371 
			
			x = temp2%10;
			int i;
			basamak_toplam = 1;
			for(i=0;i<basamak_sayisi;i++){
				basamak_toplam*=x;
				System.out.println(basamak_toplam);
				System.out.println();
			}
			temp2 = temp2/10;
			toplam += basamak_toplam;
		}
		
		if(toplam == sayi){
			System.out.println("armstrong sayidir");
		}
		else{
			System.out.println("armstrong degil");
		}
		
	}

}

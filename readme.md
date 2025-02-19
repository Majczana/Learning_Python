# Przygotowanie do obsługi baz danych SQL na platformie Azure   
# Wprowadzenie   
 --- 
Ważne jest zrozumienie obowiązków administratora bazy danych Azure oraz powiązania z innymi rolami platformy Microsoft Intelligent Data Platform.   
   
Usługi w chmurze można podzielić na 2 zestawy:   
- Infrastruktura jako usługa (LaaS)   
- Platforma jako usługa (PaaS)   
   
Usługi LaaS zazwyczaj składająsię z maszyn wirtualnych, pamięci masowej i komponentów sieci wirtualnych i są w dużej mierze zarządzane przez użytkownika (Pod względem łatania i oprogramowania).   
Natomiast PaaS alternatywnie do usługi LaaS mają większy procent zadań zarządzania, które są obsługiwane przez dostawce chmury.   
## Cele   
 --- 
- Poznaj rolę administratora bazy danych Azure i inne role platformy danych   
- Opisz najważniejsze różnice między opcjami baz danych opartych na SQL Server w usłudze Azure   
- Opisz inne funkcje dostępne na platformach Azure SQL   
   
# Role w platformie Microsoft Intelligent Data Platform   
 --- 
Microsoft oferuje 5 różnych ról dla osób które główne obowiązki zawodowe dotyczą skoncentrowanych danych w chmurze:   
|                                                                                                            **Rola** |                                                                                                                                                                                                                                                                                                                                                                                                                  **Definicja** |
|:--------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                         Inżynier danych Azure / Azure Data Engineer |                                                                                                                                                                                                                                                 Zaprojektuj i wdróż zarządzanie, monitorowanie, bezpieczeństwo i prywatność danych przy użyciu pełnego zestawu usług danych platformy Azure, aby zaspokoić potrzeby biznesowe. |
|                                                                          Analityk danych Azure / Azure Data Analyst |                    Umożliwiaj firmom maksymalizację wartości ich zasobów danych za pomocą Microsoft Power BI. Jako eksperci przedmiotowi, analitycy danych są odpowiedzialni za projektowanie i budowanie skalowalnych modeli danych, czyszczenie i transformację danych oraz włączanie zaawansowanych możliwości analitycznych, które zapewniają znaczącą wartość biznesową poprzez łatwe do zrozumienia wizualizacje danych. |
|                                                                   Naukowiec ds. danych Azure / Azure Data Scientist |                                                                                                                                                                                                                        Wykorzystuje wiedzę z zakresu nauki o danych i uczenia maszynowego do wdrażania i uruchamiania obciążeń uczenia maszynowego w usłudze Azure, w szczególności przy użyciu usługi Azure Machine Learning. |
|                                      Inżynier sztucznej inteligencji Azure / Azure Artificial Intelligence Engineer |                                                                                                                                                                                                   Wykorzystaj usługi Cognitive Services, uczenie maszynowe i eksplorację wiedzy do projektowania i wdrażania rozwiązań Microsoft AI obejmujących przetwarzanie języka naturalnego, mowę, widzenie komputerowe, boty i agentów. |
| [Administrator bazy danych Azure ](przygotowanie-do-obslugi-baz-danych-sql-na-pla.md)/ Azure Database Administrator |                                                             Wdraża i zarządza aspektami operacyjnymi rozwiązań platformy danych w chmurze i hybrydowych opartych na usługach danych Microsoft Azure i Microsoft SQL Server. Administrator bazy danych Azure używa różnych metod i narzędzi do wykonywania codziennych operacji, w tym stosowania wiedzy na temat używania języka T-SQL do celów zarządzania administracyjnego. |

# Omówienie programu SQL Server na maszynie wirtualnej platformy Azure   
 --- 
Serwer SQL uruchomiony na maszynie wirtualnej Azure LaaS jest odpowiednikiem lokanlego SQL Server. Kilka funkcji opisanych dla SQL na maszynie wirtualnej ma zastosowanie do wszystkich lokalnych serwerów SQL Server.   
Wiele aplikacji będzie wymagać uruchomienia SQL server na maszynie wirtualnej ponieważ:   
- **Wsparcie aplikacji i zgodność wersji** - niektóre aplikacje mogą działać tylko na odpowiedniej wersji SQL Server.   
- **Korzystanie z innych usług SQL server - **aby zmaksymalizować korzyści z licencji, wielu użytkowników decyduje się na uruchamianie usług SQL Server Analysis Services (SSAS), SQL Server Integration Services (SSIS) i/lub SQL Server Reporting Services (SSRS) na tym samym komputerze, na którym znajduje się moduł bazy danych.   
   
## Dostępne Wersje programu SQL Server   
 --- 
Microsoft przechowuje obrazy wszystkich wersji programu dostępnych w Azure Marketplace.    
## Tworzenie kopii zapasowej   
 --- 
Najważniejsze funkcje tworzenia kopii zapasowej:   
- **Kopia zapasowa do adresu URL (Back up to URL)** - Standardowe korzystanie z kopii zapasowej baz danych w usłudze Azure Blob Storage.   
- **Kopia zapasowa Azure (Azure Backup) -** Usługa dla maszyn wirtualnych SQL Server to kompletne rozwiązane do tworzenia kopii zapasowych dla przedsiębiorstw, które automatycznie obsługuje kopie zapasowe w całej infrastrukturze.   
   
## Opcje wdrażania   
 --- 
Wszystkie zasoby w Azure mają jednego dostawce czyli Azure Resource Manager, która działa jako usługa do zarządzania i wdrażania usług w chmurze. Istnieje wiele sposobów wdrażania zasobów Azure, ostatecznie wszystkie trafiają do dokumentów [JSON](przygotowanie-do-obslugi-baz-danych-sql-na-pla.md) znanych jako Azure Resource Manager.   
Szablon Azure Resource Manager to jedyne deklaratywne podejście do wdrażania opisujące strukturę i stan zasobów do wdrożenia. Wszystkie inne metody można opisać jako imperatywne.   
W przypadku wdrożeń na dużą skalę podejście deklaratywne jest lepsze i należy je stosować. Czyli Szablon Azure Resource Manager.   
## Omówienie usługi Azure Storage   
 --- 
Azure oferuje w pełni redundantny *(Czyli zduplikowany, odporny na awarie). *Przy projektowaniu i wdrażaniu architektury maszyn wirtualnych należy pamiętać o kilku kwestiach. Jeżeli chodzi o maszyny wirtualne można użyć 4 typów pamięci masowej:   
- Standard   
- Standardowy dysk SSD   
- Dysk SSD klasy premium   
- Ultra dysk   
   
W przypadku danych produkcyjnych i dziennika transakcji SQL Server należy używać tylko Premium SSD i Ultra Disk. Dla pamięci masowej opóźnienia będą wynosić od 5 do 10 ms. Dla ultra disk opóźnienia moga wynosić poniżej 1 ms ale w paraktyce wyniosą od 1-2 ms.    
Do tworzenia kopii zapasowej można użyć pamięci Standard ponieważ wystarczy.    
## Wysoka dostępność na platformie Azure   
Platforma Azure została tak stworzona, aby była odporna na uszkodzenia, a w razie problemów jak najszybsze odzyskanie po zakłóceniach usługi. Gwarancja czasu działania maszyny do 99,9% czyli większość czasu. (W Przypadku korzystania z dysków SSD premium i Ultra Disk)   
   

<h2>Global Services Change Management Procedure</h2>
<h3>1 Purpose</h3>
<p>This recipe establishes a standardized and structured procedure for managing changes to Global Services (GS) within the WIS 2.0 environment. It defines the end-to-end process from change proposal, impact assessment, testing, and approval to implementation and post-validation. The goal is to ensure all changes are carried out with minimized operational risk and guaranteed compliance, thereby safeguarding the normal operation of WIS 2.0.</p>
<h3>2 Scope</h3>
<p>This procedure applies to all operators of WIS 2.0 Global Services (Global Brokers, Global Caches, Global Discovery Catalogues, Global Monitors, GTS-WIS2 gateways, WIS2-GTS gateways) for the following types of changes (including, but not limited to):</p>
<ul>
<li><strong>Infrastructure Changes</strong>: IP address, network configuration, hardware replacement or scaling.</li>
<li><strong>Software Changes</strong>: Core software version upgrades, patch deployment, addition/removal of functional modules.</li>
<li><strong>Deployment &amp; Topology Changes</strong>: Service migration to new environments (e.g., cloud), architectural adjustments, redundancy configuration changes.</li>
<li><strong>Security &amp; Compliance Changes</strong>: Certificate renewal, major adjustments to access control policies.</li>
<li><strong>Service Level &amp; Policy Changes</strong>: Data retention policy, service availability target adjustments.</li>
</ul>
<h3>3 Roles and Responsibilities</h3>
<ul>
<li><strong>Global Service (GS) Operator</strong>: Proposes changes, provides detailed plans and migration procedures, executes changes, and performs self verification.</li>
<li><strong>WMO Secretariat</strong>: Acts as the process coordinator. Receives proposals, conducts initial impact assessment, distributes for review, notifies the community, and oversees the entire process.</li>
<li><strong>ET-WISOP</strong>: Serves as the change implementation approval body. Responsible for assessing the potential impact of changes, reviewing implementation plans, deciding on the need for additional testing, and providing feedback to minimize operational risk for WIS 2.0.</li>
<li><strong>Test Team</strong>: Independently retests and validates the changed Global Service according to the WIS 2.0 Test Plan to ensure compliance with WIS 2.0 technical specifications.</li>
<li><strong>GISCs</strong>: After implementation, responsible for checking the operational status of all WIS2 Nodes in their Area of Responsibility to ensure proper functioning.</li>
<li><strong>WIS2 Node</strong>: Receives change notifications, update the Global Service information and provides feedback for changes that may affect them.</li>
</ul>
<h3>4 Change Classification and Lead Time</h3>
<p>Different management paths and lead times are defined based on the nature and impact of the change:</p>

Change Classification | Description | Minimum Lead Time | Key Process Requirements
-- | -- | -- | --
IP Address Change | Change only the network endpoint address of the service. | 2 weeks | The WMO Secretariat shall notify the community in advance; GISCs should verify node status post-implementation.
Limited-Impact Change | Changes with limited impact on WIS2 Node or Global Service operations, e.g., internal optimizations, non-critical patches. | 2 weeks | After rapid review and endorsement by ET-WISOP, can be executed within a week and deployed after successful retesting.
Significant Change | Changes that may affect WIS2 Node or Global Service operations, e.g., major software upgrades, architectural refactoring. | 8 weeks | Shall be notified to the community by the WMO Secretariat at least one week in advance; requires detailed assessment by ET-WISOP and retesting by the Test Team.


<p><strong>Note</strong>: A planning lead time of 2 to 8 weeks is required for all changes to ensure adequate planning and execution.</p>
<h3>5 Standard Change Management Process</h3>
<p>This section describes the complete lifecycle of a change from proposal to closure.</p>
<h4>5.1 Process Overview and Entry Point</h4>
<ol>
<li><strong>Submission of Request</strong>: The GS Operator identifies a change requirement, prepares a Change Request including: change description, technical details, preliminary impact analysis, proposed implementation window, and rollback plan. The request is formally submitted to the WMO Secretariat.</li>
<li><strong>Initial Receipt and Classification</strong>: The WMO Secretariat receives the request and conducts a preliminary review. The core decision point is the nature of the change:
<ul>
<li><strong>Decision A: Is it only an IP address change?</strong> → Proceed to the <strong>IP Address Change Process</strong>.</li>
<li><strong>Decision B: Is it another type of change?</strong> → Proceed to the <strong>Other Change Process</strong>, where impact will be further assessed by ET-WISOP.</li>
</ul>
</li>
</ol>
<h4>5.2 Path One: IP Address Change Process</h4>
<p>This path applies to scenarios involving only the modification of a service's network endpoint.</p>
<ol start="1">
<li><strong>Coordination and Scheduling</strong>: The WMO Secretariat checks the global change calendar to coordinate a suitable implementation time, avoiding conflicts with other GS change plans. The confirmed schedule is communicated back to the GS Operator.</li>
<li><strong>Community Notification</strong>: Before the planned implementation date, the WMO Secretariat is responsible for notifying the WIS 2.0 community in advance, informing them of the GS involved, old and new IP addresses, planned switchover time, and recommended actions.</li>
<li><strong>WIS2 Node update</strong>: The WIS2 Nodes shall update the Global Service information, and open the ACL for the new IP(s) of the Global Service.</li>
<li><strong>Implementation Preparation</strong>: The GS Operator prepares for the switchover as scheduled. If a technical switchover procedure is required, it should be submitted to the WMO Secretariat for record.</li>
<li><strong>Execution of Change</strong>: Within the approved time window, the GS Operator executes the IP address change operation.</li>
<li><strong>Verification</strong>: GISCs verify that the WIS2 Nodes in their Area of Responsibility can be connect normally by the Global Service.</li>
<li><strong>Process Closure</strong>: Upon receiving positive verification feedback from the GISCs, the WMO Secretariat confirms no anomalies and declares the change complete.</li>
</ol>
<h4>5.3 Path Two: Other Change Process</h4>
<p>This path applies to changes involving software, deployment, functionality, etc., that are not purely IP-related. The ET-WISOP is the core assessment and approval authority in this path.</p>
<ol start="1">
<li><strong>Submission for Technical Assessment</strong>: The WMO Secretariat forwards the change details and migration procedure draft submitted by the GS Operator to the ET-WISOP Expert Team, requesting an impact assessment.</li>
<li><strong>Impact Assessment and Routing</strong>: ET-WISOP reviews the change and makes a key determination:
<ul>
<li><strong>Decision C: The change has limited impact</strong> → Proceed to the <strong>Limited-Impact Change Sub-process</strong>.</li>
<li><strong>Decision D: The change has significant impact</strong> (may affect node or GS operations) → Proceed to the <strong>Significant-Impact Change Sub-process</strong>.</li>
</ul>
</li>
</ol>
<h5>5.3.1 Sub-process A: Limited-Impact Change</h5>
<ol start="1">
<li><strong>Rapid Endorsement</strong>: ET-WISOP formally replies to the WMO Secretariat with the conclusion "change has limited impact" and recommends "the GS Operator may be notified to proceed".</li>
<li><strong>Authorization to Execute</strong>: The WMO Secretariat notifies the GS Operator of ET-WISOP's conclusion, authorizing them to proceed with the change.</li>
<li><strong>Implementation</strong>: Upon receiving authorization, the GS Operator could execute the change.</li>
<li><strong>Completion Confirmation</strong>: The GS Operator reports the completion of the change to the WMO Secretariat. After recording, the WMO Secretariat can close the process. GISCs observe node status as part of their routine monitoring duties.</li>
</ol>
<h5>5.3.2 Sub-process B: Significant-Impact Change</h5>
<ol start="1">
<li><strong>Community Pre-Notification</strong>: Concurrently with or shortly after ET-WISOP's assessment, the WMO Secretariat should notify the WIS 2.0 community at least one week in advance, informing them of the upcoming significant change and its potential impact.</li>
<li><strong>Retest Decision and Execution</strong>:
<ul>
<li>ET-WISOP typically requires a formal retest for significant changes. The WMO Secretariat coordinates between the Test Team and the GS Operator.</li>
<li>The Test Team performs an independent retest of the changed service in a test environment, following the WIS 2.0 Test Plan.</li>
<li>The retest report is submitted to the WMO Secretariat and ET-WISOP. Successful passage is a prerequisite for the subsequent process.</li>
</ul>
</li>
<li><strong>Switchover Procedure Review</strong>:
<ul>
<li>The GS Operator must provide a detailed switchover procedure (e.g., deployment plan, parallel operation).</li>
<li>ET-WISOP conducts a collective review of the switchover procedure, assesses its operational risk, and provides feedback for modification, aiming to minimize the risk of disruption to WIS 2.0 operations.</li>
</ul>
</li>
<li><strong>Final Approval</strong>: After successful retesting and ET-WISOP's acceptance of the switchover procedure, the WMO Secretariat grants the GS Operator final approval for implementation.</li>
<li><strong>Execution of Change</strong>: Within the approved time window, the GS Operator executes the change strictly according to the reviewed procedure.</li>
<li><strong>Post-Implementation Mandatory Verification</strong>:
<ul>
<li>After implementation, all GISCs shall, within a specified period (e.g., 24 hours),comprehensively verify the operational status of all WIS2 Nodes in their Area of Responsibility.</li>
<li>The GS Operator monitors its own service's key performance indicators.</li>
</ul>
</li>
<li><strong>Process Closure</strong>: The WMO Secretariat consolidates the verification results from GISCs and the status report from the GS Operator. Upon confirming that the global impact is under control, the change process is formally closed.</li>
</ol>
<h3>6 General Best Practices</h3>
<ul>
<li><strong>Parallel Operation</strong>: Whenever possible, switchover procedures should consider strategies for parallel operation of old and new versions to provide a rollback buffer and validate the stability of the new version.</li>
<li><strong>Communication Records</strong>: All key step communications (e.g., community notifications, assessment conclusions, approval instructions) should be conducted through formal channels (email, official announcements) and documented.</li>
<li><strong>Change Calendar</strong>: The WMO Secretariat should maintain a global change calendar for coordination and conflict avoidance.</li>
</ul>
<a href="./Global_Services_Change_Management_Procedure_Flowchart.pdf">Global Services Change Management Procedure Flowchart.pdf</a>
